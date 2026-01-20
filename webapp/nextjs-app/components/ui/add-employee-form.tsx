"use client";

import { createEmployee } from "@/actions/employee";
import { useState, useRef } from "react";

export default function AddEmployeeForm() {
    const [open, setOpen] = useState(false);
    const formRef = useRef<HTMLFormElement>(null);
    const [msg, setMsg] = useState("");

    async function clientAction(formData: FormData) {
        const res = await createEmployee(formData);
        if (res.success) {
            setMsg("Employee added!");
            formRef.current?.reset();
            setTimeout(() => setMsg(""), 3000);
            setOpen(false);
        } else {
            setMsg(res.error || "Error");
        }
    }

    if (!open) {
        return (
            <button
                onClick={() => setOpen(true)}
                className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition"
            >
                + Add Employee
            </button>
        )
    }

    return (
        <div className="bg-white dark:bg-gray-900 p-4 rounded-md border shadow-sm mb-6">
            <div className="flex justify-between items-center mb-4">
                <h3 className="font-semibold">New Employee Record</h3>
                <button onClick={() => setOpen(false)} className="text-gray-500 hover:text-gray-700">Cancel</button>
            </div>

            {msg && <p className="text-sm mb-2 text-indigo-600">{msg}</p>}

            <form ref={formRef} action={clientAction} className="grid gap-4 sm:grid-cols-2">
                <input name="firstName" placeholder="First Name" required className="border rounded px-3 py-2 bg-transparent" />
                <input name="lastName" placeholder="Last Name" required className="border rounded px-3 py-2 bg-transparent" />
                <input name="email" type="email" placeholder="Email" required className="border rounded px-3 py-2 bg-transparent" />
                <input name="position" placeholder="Position" required className="border rounded px-3 py-2 bg-transparent" />
                <input name="department" placeholder="Department" required className="border rounded px-3 py-2 bg-transparent" />
                <input name="salary" type="number" step="0.01" placeholder="Salary" required className="border rounded px-3 py-2 bg-transparent" />
                <input name="dateHired" type="date" required className="border rounded px-3 py-2 bg-transparent" />

                <div className="sm:col-span-2">
                    <button type="submit" className="w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-700">
                        Save Record
                    </button>
                </div>
            </form>
        </div>
    );
}
