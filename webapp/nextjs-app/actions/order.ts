"use server";

import { z } from "zod";
import { prisma } from "@/lib/prisma";
import { revalidatePath } from "next/cache";

const orderSchema = z.object({
    clientName: z.string().min(1, "Name is required"),
    clientEmail: z.string().email("Invalid email"),
    companyName: z.string().optional(),
    plan: z.enum(["STANDARD", "PROFESSIONAL", "ENTERPRISE"]),
    message: z.string().optional(),
});

export async function createOrder(formData: FormData) {
    const rawData = {
        clientName: formData.get("clientName"),
        clientEmail: formData.get("clientEmail"),
        companyName: formData.get("companyName"),
        plan: formData.get("plan"),
        message: formData.get("message"),
    };

    const validate = orderSchema.safeParse(rawData);

    if (!validate.success) {
        return { success: false, error: validate.error.errors[0].message };
    }

    try {
        await prisma.order.create({
            data: {
                clientName: validate.data.clientName,
                clientEmail: validate.data.clientEmail,
                companyName: validate.data.companyName,
                plan: validate.data.plan,
                message: validate.data.message,
            },
        });

        revalidatePath("/dashboard/orders"); // If/when we have an admin view
        return { success: true };
    } catch (error) {
        console.error("Order creation failed:", error);
        return { success: false, error: "Database error. Please try again." };
    }
}
