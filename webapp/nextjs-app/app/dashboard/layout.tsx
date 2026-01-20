
import { auth, signOut } from "@/auth";
import Link from "next/link";
import { Users, LayoutDashboard, LogOut } from "lucide-react";

export default async function DashboardLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    const session = await auth();
    const role = session?.user?.role;
    const isHR = role === "HR" || role === "CEO";

    return (
        <div className="flex min-h-screen">
            {/* Sidebar */}
            <aside className="w-64 bg-gray-900 text-white shrink-0 hidden md:block">
                <div className="p-6">
                    <h2 className="text-xl font-bold">AtlasIntranet</h2>
                    <p className="text-xs text-gray-400 mt-1">Logged in as {session?.user?.name || "User"} ({role})</p>
                </div>
                <nav className="px-4 space-y-2 mt-4">
                    <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-gray-800 transition-colors">
                        <LayoutDashboard size={20} />
                        Dashboard
                    </Link>

                    {isHR && (
                        <Link href="/dashboard/hr" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-gray-800 transition-colors text-red-300">
                            <Users size={20} />
                            HR Management (Secure)
                        </Link>
                    )}

                    <form action={async () => {
                        "use server"
                        await signOut()
                    }}>
                        <button className="w-full flex items-center gap-3 px-3 py-2 rounded hover:bg-red-900/50 text-red-400 transition-colors mt-8">
                            <LogOut size={20} />
                            Sign Out
                        </button>
                    </form>
                </nav>
            </aside>

            {/* Main Content */}
            <main className="flex-1 bg-gray-50 dark:bg-gray-950">
                <div className="p-8">
                    {children}
                </div>
            </main>
        </div>
    );
}
