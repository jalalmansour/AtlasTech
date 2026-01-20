"use server";

import { z } from "zod";
import { prisma } from "@/lib/prisma";
import { revalidatePath } from "next/cache";
import { auth } from "@/auth";

const employeeSchema = z.object({
    firstName: z.string().min(1),
    lastName: z.string().min(1),
    email: z.string().email(),
    position: z.string().min(1),
    department: z.string().min(1),
    salary: z.coerce.number().positive(),
    dateHired: z.string().transform((str) => new Date(str)),
});

export async function createEmployee(formData: FormData) {
    const session = await auth();
    const role = session?.user?.role;

    if (role !== "HR" && role !== "CEO") {
        return { success: false, error: "Unauthorized" };
    }

    const rawData = {
        firstName: formData.get("firstName"),
        lastName: formData.get("lastName"),
        email: formData.get("email"),
        position: formData.get("position"),
        department: formData.get("department"),
        salary: formData.get("salary"),
        dateHired: formData.get("dateHired"),
    };

    const validate = employeeSchema.safeParse(rawData);

    if (!validate.success) {
        return { success: false, error: validate.error.errors[0].message };
    }

    try {
        await prisma.employee.create({
            data: validate.data,
        });

        revalidatePath("/dashboard/hr");
        return { success: true };
    } catch (error) {
        console.error("Employee creation failed:", error);
        return { success: false, error: "Database error." };
    }
}

export async function deleteEmployee(id: string) {
    const session = await auth();
    const role = session?.user?.role;

    if (role !== "HR" && role !== "CEO") {
        return { success: false, error: "Unauthorized" };
    }

    try {
        await prisma.employee.delete({ where: { id } });
        revalidatePath("/dashboard/hr");
        return { success: true };
    } catch (error) {
        return { success: false, error: "Failed to delete" };
    }
}
