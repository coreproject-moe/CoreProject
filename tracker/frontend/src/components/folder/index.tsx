import React, { ReactNode } from "react";
import styles from "./index.module.css";
import { cn } from "@/lib/utils";

type FolderProps = {
  children?: ReactNode;
  className?: string;
};

export const FolderDiv: React.FC<FolderProps> = ({ children, className }) => {
  return (
    <div
      className={cn(
        className,
        `${styles.folder}`,
        `rounded-tl-4 relative flex h-64 w-96 rounded-tr-3xl rounded-br-3xl rounded-bl-3xl bg-white`,
        `before:absolute before:-top-[18px] before:h-5 before:w-96 before:rounded-tl-3xl before:bg-white before:content-['']`,
      )}
    >
      {children}
    </div>
  );
};
