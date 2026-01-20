import Link from "next/link";
import { ArrowRight, Shield, Server, Lock, CheckCircle } from "lucide-react";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Navigation */}
      <header className="px-4 lg:px-6 h-14 flex items-center border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 sticky top-0 z-50">
        <Link className="flex items-center justify-center font-bold text-xl" href="#">
          <Shield className="h-6 w-6 mr-2 text-primary" />
          AtlasTech Solutions
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#services">
            Services
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#about">
            About
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#contact">
            Contact
          </Link>
        </nav>
      </header>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-gray-50 dark:bg-gray-900">
          <div className="container px-4 md:px-6 mx-auto">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                  Secure Digital Transformation
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  AtlasTech provides enterprise-grade web development, hosting, and security solutions.
                  Building the future, securely.
                </p>
              </div>
              <div className="space-x-4">
                <Link
                  className="inline-flex h-9 items-center justify-center rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                  href="#contact"
                >
                  Get Started
                </Link>
                <Link
                  className="inline-flex h-9 items-center justify-center rounded-md border border-gray-200 bg-white px-4 py-2 text-sm font-medium shadow-sm transition-colors hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
                  href="#services"
                >
                  View Services
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* Service Packs */}
        <section id="services" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6 mx-auto">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <div className="inline-block rounded-lg bg-gray-100 px-3 py-1 text-sm dark:bg-gray-800">
                  Our Offerings
                </div>
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Service Packs</h2>
                <p className="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Choose the right level of support for your business needs.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3 lg:gap-12">

              {/* Basic Pack */}
              <div className="flex flex-col justify-between rounded-lg border bg-card text-card-foreground shadow-sm p-6 space-y-4">
                <div className="space-y-2">
                  <h3 className="text-2xl font-bold">Standard</h3>
                  <p className="text-sm text-muted-foreground">Essential web presence.</p>
                </div>
                <ul className="grid gap-2 py-4">
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Basic Hosting
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> CMS Integration
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Email Support
                  </li>
                </ul>
                <div className="mt-auto">
                  <p className="text-3xl font-bold mb-4">$499<span className="text-sm font-normal text-muted-foreground">/mo</span></p>
                  <Link href="/order?plan=standard" className="w-full inline-flex h-10 items-center justify-center rounded-md bg-primary text-primary-foreground font-medium shadow transition-colors hover:bg-primary/90">
                    Select Plan
                  </Link>
                </div>
              </div>

              {/* Pro Pack */}
              <div className="flex flex-col justify-between rounded-lg border bg-card text-card-foreground shadow-sm p-6 space-y-4 border-primary">
                <div className="space-y-2">
                  <h3 className="text-2xl font-bold">Professional</h3>
                  <p className="text-sm text-muted-foreground">For growing businesses.</p>
                </div>
                <ul className="grid gap-2 py-4">
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Dedicated VPS
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> 24/7 Priority Support
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Monthly Audits
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Custom Development
                  </li>
                </ul>
                <div className="mt-auto">
                  <p className="text-3xl font-bold mb-4">$999<span className="text-sm font-normal text-muted-foreground">/mo</span></p>
                  <Link href="/order?plan=professional" className="w-full inline-flex h-10 items-center justify-center rounded-md bg-primary text-primary-foreground font-medium shadow transition-colors hover:bg-primary/90">
                    Select Plan
                  </Link>
                </div>
              </div>

              {/* Enterprise Pack */}
              <div className="flex flex-col justify-between rounded-lg border bg-card text-card-foreground shadow-sm p-6 space-y-4">
                <div className="space-y-2">
                  <h3 className="text-2xl font-bold">Enterprise</h3>
                  <p className="text-sm text-muted-foreground">Maximum security & scale.</p>
                </div>
                <ul className="grid gap-2 py-4">
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Private Cloud
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Dedicated Dev Team
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> SLA Guarantee
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="h-4 w-4" /> Advanced Security
                  </li>
                </ul>
                <div className="mt-auto">
                  <p className="text-3xl font-bold mb-4">Contact Us<span className="text-sm font-normal text-muted-foreground">/mo</span></p>
                  <Link href="/order?plan=enterprise" className="w-full inline-flex h-10 items-center justify-center rounded-md bg-primary text-primary-foreground font-medium shadow transition-colors hover:bg-primary/90">
                    Select Plan
                  </Link>
                </div>
              </div>

            </div>
          </div>
        </section>

        {/* Contact/Order Section */}
        <section id="contact" className="w-full py-12 md:py-24 lg:py-32 bg-gray-50 dark:bg-gray-900">
          <div className="container px-4 md:px-6 mx-auto">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl">Ready to Start?</h2>
              <p className="max-w-[600px] text-gray-500 md:text-xl dark:text-gray-400">
                Contact us to discuss your project requirements.
              </p>
              <Link href="/order" className="inline-flex h-10 items-center justify-center rounded-md bg-gray-900 px-8 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300">
                Go to Order Form
              </Link>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
        <p className="text-xs text-gray-500 dark:text-gray-400">© 2026 AtlasTech Solutions. All rights reserved.</p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Terms of Service
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Privacy
          </Link>
        </nav>
      </footer>
    </div>
  );
}
