import React from "react";
import { Flex } from "@chakra-ui/react";
import { LoginHeader } from "@components/LoginHeader";
import { LoginBody } from "@components/LoginBody";

export const Login = () => {
  return (
    <>
      <LoginHeader />
      <LoginBody title="Driver"/>
    </>
  );
};
