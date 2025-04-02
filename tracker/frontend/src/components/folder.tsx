import React, { ReactNode } from "react";

type FolderProps = {
  children?: ReactNode;
};

export const FolderDiv: React.FC<FolderProps> = ({ children }) => {
  return (
    <div className="before:clip-path-[path('M_0_0_L_160_0_C_185_2,_175_16,_200_18_L_0_50_z')] relative h-[310px] w-[420px] rounded-tl-[5px] rounded-tr-[25px] rounded-br-[25px] rounded-bl-[25px] bg-white before:absolute before:-top-[18px] before:h-[25px] before:w-[200px] before:rounded-[25px_0_0_0] before:bg-white before:content-['']">
      {children}
    </div>
  );
};
