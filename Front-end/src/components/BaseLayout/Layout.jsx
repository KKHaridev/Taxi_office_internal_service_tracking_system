import React from "react";
import { SideBar } from "@components";
import { Outlet } from "react-router-dom";
import { Header } from "@components";
import { Box } from "@chakra-ui/react";

export const Layout = () => {
  return (
    <>
      <Header />
      <SideBar />
      <Box
        marginLeft="80px"
        padding="10px"
        bg="red"
        h="calc(100vh - 70px)"
        w="calc(100vw - 90px)"
      >
        <Outlet />
      </Box>
    </>
  );
};
