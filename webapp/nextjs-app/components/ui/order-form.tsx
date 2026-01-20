"use client";

import { useSearchParams } from "next/navigation";
import { useState } from "react";
// import { createOrder } from "@/actions/order"; 

export default function OrderForm() {
    const searchParams = useSearchParams();
    const defaultPlan = searchParams.get("plan") || "STANDARD";

    const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
    const [message, setMessage] = useState("");

    async function handleSubmit(formData: FormData) {
        setStatus("submitting");
        const result = await createOrder(formData);
        if (result.success) {
            setStatus("success");
            setMessage("Order placed successfully! We will contact you shortly.");
        } else {
            setStatus("error");
            setMessage(result.error || "Something went wrong.");
        }
    }

    if (status === "success") {
        return (
            <div className="text-center py-10 space-y-4">
                <div className="text-green-500 text-5xl mb-4">✓</div>
                <h3 className="text-2xl font-bold">Request Received</h3>
                <p className="text-gray-500">{message}</p>
                <button onClick={() => setStatus("idle")} className="text-primary hover:underline">
                    Submit another request
                </button>
            </div>
        );
    }

    return (
        <form action={handleSubmit} className="space-y-4">
            <div className="space-y-2">
                <label htmlFor="clientName" className="text-sm font-medium leading-none">
                    Full Name
                </label>
                <input
                    id="clientName"
                    name="clientName"
                    required
                    className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                    placeholder="John Doe"
                />
            </div>

            <div className="space-y-2">
                <label htmlFor="clientEmail" className="text-sm font-medium leading-none">
                    Email
                </label>
                <input
                    id="clientEmail"
                    name="clientEmail"
                    type="email"
                    required
                    className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                    placeholder="john@example.com"
                />
            </div>

            <div className="space-y-2">
                <label htmlFor="companyName" className="text-sm font-medium leading-none">
                    Company (Optional)
                </label>
                <input
                    id="companyName"
                    name="companyName"
                    className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                    placeholder="Acme Inc."
                />
            </div>

            <div className="space-y-2">
                <label htmlFor="plan" className="text-sm font-medium leading-none">
                    Service Pack
                </label>
                <select
                    id="plan"
                    name="plan"
                    defaultValue={defaultPlan}
                    className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                >
                    <option value="STANDARD">Standard</option>
                    <option value="PROFESSIONAL">Professional</option>
                    <option value="ENTERPRISE">Enterprise</option>
                </select>
            </div>

            <div className="space-y-2">
                <label htmlFor="message" className="text-sm font-medium leading-none">
                    Message
                </label>
                <textarea
                    id="message"
                    name="message"
                    className="flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                    placeholder="Tell us about your project..."
                />
            </div>

            <button
                type="submit"
                disabled={status === "submitting"}
                className="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 w-full"
            >
                {status === "submitting" ? "Submitting..." : "Submit Request"}
            </button>

            {status === "error" && (
                <p className="text-sm text-red-500 text-center">{message}</p>
            )}
        </form>
    );
}
