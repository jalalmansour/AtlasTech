import { auth } from "@/auth";
import { NextResponse } from "next/server";

export default auth((req) => {
    const isLoggedIn = !!req.auth;
    const isOnDashboard = req.nextUrl.pathname.startsWith("/dashboard");
    const isHRRoute = req.nextUrl.pathname.startsWith("/dashboard/hr");

    if (isOnDashboard) {
        if (!isLoggedIn) {
            return NextResponse.redirect(new URL("/login", req.nextUrl));
        }

        // RBAC: strict access to HR module
        if (isHRRoute) {
            // Only HR and CEO can access HR module
            const role = req.auth?.user?.role;
            if (role !== "HR" && role !== "CEO") {
                // Redirect to general dashboard with unauthorized error? 
                // Or just generic dashboard
                return NextResponse.redirect(new URL("/dashboard", req.nextUrl));
            }
        }
    }

    return NextResponse.next();
});

export const config = {
    // Matched paths
    matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
