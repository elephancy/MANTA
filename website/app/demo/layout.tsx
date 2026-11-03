import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = {
  title: "MANTA interactive demo — mobile traffic anomaly detection",
  description:
    "Explore a simulated Android traffic-monitoring app, its anomaly decision trace and privacy controls in the MANTA thesis demo.",
  alternates: { canonical: "https://bachelor.elfeel.me/demo" },
};

export default function DemoLayout({ children }: { children: ReactNode }) {
  return children;
}
