import React from "react";
import { Box } from "@chakra-ui/react";

export const TableHolder = ({ children }) => {
  return (
    <Box overflow="auto" minHeight="85vh">
      {children}
    </Box>
  );
};
