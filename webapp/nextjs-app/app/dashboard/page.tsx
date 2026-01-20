import { auth } from "@/auth";

export default async function DashboardPage() {
    const session = await auth();

    return (
        <div>
            <h1 className="text-3xl font-bold mb-4">Welcome back, {session?.user?.name}</h1>
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                <div className="p-6 bg-white dark:bg-gray-900 rounded-lg shadow">
                    <h3 className="font-semibold mb-2">My Profile</h3>
                    <p className="text-sm text-gray-500">View and edit your profile settings.</p>
                </div>
                <div className="p-6 bg-white dark:bg-gray-900 rounded-lg shadow">
                    <h3 className="font-semibold mb-2">Company News</h3>
                    <p className="text-sm text-gray-500">Latest updates from AtlasTech.</p>
                </div>
            </div>
        </div>
    )
}
