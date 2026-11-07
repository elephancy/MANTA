import type { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    { url: "https://bachelor.elfeel.me/" },
    { url: "https://bachelor.elfeel.me/demo" },
  ];
}
