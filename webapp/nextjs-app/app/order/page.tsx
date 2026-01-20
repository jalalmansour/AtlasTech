import { Suspense } from "react";
import OrderForm from "@/components/ui/order-form";

export default function OrderPage() {
    return (
        <div className="flex flex-col min-h-screen">
            <header className="px-4 lg:px-6 h-14 flex items-center border-b">
                <h1 className="text-xl font-bold">AtlasTech Order System</h1>
            </header>
            <main className="flex-1 container px-4 py-8 mx-auto max-w-2xl">
                <h2 className="text-3xl font-bold mb-6">Request Service</h2>
                <div className="bg-card border rounded-lg p-6 shadow-sm">
                    <Suspense fallback={<div>Loading form...</div>}>
                        <OrderForm />
                    </Suspense>
                </div>
            </main>
        </div>
    );
}
