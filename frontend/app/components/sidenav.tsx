"use client";
import { Drawer, List, ListItem, Toolbar } from "@mui/material";
import Link from "next/link";

const navLinks = [
  { name: "Channel", href: "/channel" },
  { name: "Content", href: "/content" },
  { name: "Catalog", href: "/catalog" },
];

export default function SideNav() {
  return (
    <Drawer variant="permanent" sx={{ width: "240px" }}>
      <Toolbar />
      <List sx={{ width: "240px" }}>
        {navLinks.map((link) => (
          <ListItem key={link.name}>
            <Link href={link.href}>{link.name}</Link>
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}
