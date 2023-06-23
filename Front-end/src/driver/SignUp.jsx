import React, { useContext, useState } from "react";
import { Container, Heading, Flex } from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import {
  FormErrorMessage,
  FormLabel,
  FormControl,
  Input,
  Button,
  Box,
  Text,
} from "@chakra-ui/react";
import { useToast } from "@chakra-ui/react";
import { LoginHeader } from "../components/LoginHeader";

import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useCreateDriver } from "../hooks/useData";
import { SignUp2 } from "../components/SigUp/SignUp2";
import { SignUp1 } from "../components/SigUp/SignUp1";
import { SignUp3 } from "../components/SigUp/SignUp3";

export const SignUp = () => {
  const [first, setFirst] = useState(false);
  const [second, setSecond] = useState(false);

  const toast = useToast();
  const { login } = useAuth();
  const navigate = useNavigate();
  const { mutate: createDriver, isSuccess } = useCreateDriver();
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
    watch,
  } = useForm();
  const onSubmit = async (values) => {
    try {
      //createDriver(values);
      values.password === values.confirm_password ? setFirst(true) : "";
    } catch (err) {
      console.log(err);
    }
  };
  const onSubmit2 = async (values) => {
    try {
      //createDriver(values);
      values.upi != values.phone ? setSecond(true) : "";
    } catch (err) {
      console.log(err);
    }
  };
  const onSubmit3 = async (values) => {
    try {
      //createDriver(values);
      values.upi != values.phone ? navigate('/login') : "";
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <>
      <LoginHeader />

      <Container
        as="section"
        maxW="100vw"
        m={0}
        px={0}
        display="flex"
        alignItems="center"
        justifyContent="center"
      >
        <Flex
          background={["white", "white", "transparent"]}
          borderRadius={["md", "lg"]}
          w={"100%"}
          flexDir="column"
          justifyContent="center"
          alignItems="center"
          zIndex={1}
          py={10}
          px={5}
          h="85vh"
        >
          <Heading
            as="h4"
            fontSize={["18px", "20px", "22px"]}
            fontWeight="500"
            mb={10}
          >
            Driver Sign Up
          </Heading>

          {first ? (
            second ? (
              <SignUp3
                submit={handleSubmit(onSubmit3)}
                register={register}
                errors={errors}
                isSubmitting={isSubmitting}
                watch={watch}
              />
            ) : (
              <SignUp2
                submit={handleSubmit(onSubmit2)}
                register={register}
                errors={errors}
                isSubmitting={isSubmitting}
                watch={watch}
              />
            )
          ) : (
            <SignUp1
              submit={handleSubmit(onSubmit)}
              register={register}
              errors={errors}
              isSubmitting={isSubmitting}
              watch={watch}
            />
          )}
        </Flex>
      </Container>
    </>
  );
};
