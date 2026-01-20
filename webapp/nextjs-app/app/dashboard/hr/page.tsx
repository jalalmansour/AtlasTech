import { prisma } from "@/lib/prisma";
import EmployeeTable from "@/components/ui/employee-table";
import AddEmployeeForm from "@/components/ui/add-employee-form";

export default async function HRDashboard() {
    const employees = await prisma.employee.findMany({
        orderBy: { createdAt: 'desc' }
    });

    return (
        <div className="space-y-6">
            <div className="flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold">HR Management</h1>
                    <p className="text-gray-500">Secure Database Access (Confidential)</p>
                </div>
            </div>

            <AddEmployeeForm />

            <EmployeeTable employees={employees} />
        </div>
    );
}
