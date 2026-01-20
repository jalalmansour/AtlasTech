import NextAuth, { type DefaultSession } from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { z } from "zod";
import { prisma } from "@/lib/prisma";
import bcrypt from "bcrypt";

// Extend session type for RBAC
declare module "next-auth" {
    interface Session {
        user: {
            id: string;
            role: string;
        } & DefaultSession["user"];
    }
    interface User {
        role: string;
    }
}

declare module "next-auth/jwt" {
    interface JWT {
        role: string;
        id: string;
    }
}

export const { handlers, signIn, signOut, auth } = NextAuth({
    providers: [
        Credentials({
            credentials: {
                email: { label: "Email", type: "email" },
                password: { label: "Password", type: "password" },
            },
            authorize: async (credentials) => {
                const parsedCredentials = z
                    .object({ email: z.string().email(), password: z.string().min(6) })
                    .safeParse(credentials);

                if (parsedCredentials.success) {
                    const { email, password } = parsedCredentials.data;
                    const user = await prisma.user.findUnique({ where: { email } });

                    if (!user) return null;

                    // In real world use bcrypt.compare(password, user.password)
                    // For this lab simulation, we might seed with plain text or hashes.
                    // Let's assume hashes.
                    // const passwordsMatch = await bcrypt.compare(password, user.password);
                    // if (passwordsMatch) return user;

                    // For simplicity in the first run/seeding:
                    if (password === user.password || await bcrypt.compare(password, user.password)) return user;
                }

                console.log("Invalid credentials");
                return null;
            },
        }),
    ],
    callbacks: {
        async jwt({ token, user }) {
            if (user) {
                token.role = user.role;
                token.id = user.id;
            }
            return token;
        },
        async session({ session, token }) {
            if (token && session.user) {
                session.user.role = token.role;
                session.user.id = token.id;
            }
            return session;
        }
    },
    pages: {
        signIn: '/login', // Custom login page
    }
});
