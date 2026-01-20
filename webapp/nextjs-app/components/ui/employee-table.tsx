"use client";

import { Employee } from "@prisma/client";
import { deleteEmployee } from "@/actions/employee";
import { Trash2 } from "lucide-react";
import { useState } from "react";

export default function EmployeeTable({ employees }: { employees: Employee[] }) {

    return (
        <div className="rounded-md border">
            <table className="w-full text-sm text-left">
                <thead className="bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-200">
                    <tr>
                        <th className="px-4 py-3 font-medium">Name</th>
                        <th className="px-4 py-3 font-medium">Role</th>
                        <th className="px-4 py-3 font-medium">Department</th>
                        <th className="px-4 py-3 font-medium">Salary</th>
                        <th className="px-4 py-3 font-medium text-right">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.map((emp) => (
                        <tr key={emp.id} className="border-t hover:bg-gray-50 dark:hover:bg-gray-900">
                            <td className="px-4 py-3 font-medium">{emp.firstName} {emp.lastName}</td>
                            <td className="px-4 py-3">{emp.position}</td>
                            <td className="px-4 py-3">{emp.department}</td>
                            <td className="px-4 py-3 text-emerald-600 font-mono">${Number(emp.salary).toLocaleString()}</td>
                            <td className="px-4 py-3 text-right">
                                <form action={async () => {
                                    if (confirm("Are you sure?")) await deleteEmployee(emp.id)
                                }}>
                                    <button className="text-red-500 hover:text-red-700 transition-colors">
                                        <Trash2 size={16} />
                                    </button>
                                </form>
                            </td>
                        </tr>
                    ))}
                    {employees.length === 0 && (
                        <tr>
                            <td colSpan={5} className="px-4 py-8 text-center text-gray-500">No employees found.</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
}
