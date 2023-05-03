import React from "react";
import { Container, Heading, Flex } from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import {
  FormErrorMessage,
  FormLabel,
  FormControl,
  Input,
  Button,
} from "@chakra-ui/react";

import { useNavigate } from "react-router-dom";

export const LoginBody = ({ title }) => {
  const navigate = useNavigate();
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
  } = useForm();

  function onSubmit(values) {
    return new Promise((resolve) => {
      setTimeout(() => {
        if (values.name === values.password) {
          navigate("/dashboard", { replace: true });
        }
        resolve();
      }, 1000);
    });
  }
  return (
    <Container
      as="section"
      maxW={{
        base: "container.sm",
        md: "container.md",
        lg: "container.lg",
        xl: "container.xl",
      }}
      py={5}
      display="flex"
      alignItems="center"
      justifyContent="center"
      flexDir="column"
    >
      <Flex
        minH="calc(85vh - 120px)"
        w="400px"
        flexDir="column"
        justifyContent="center"
        alignItems="center"
      >
        <Heading as="h4" fontSize="22px" fontWeight="500" mb={10}>
          {title} Login
        </Heading>

        <form
          w={100}
          onSubmit={handleSubmit(onSubmit)}
          style={{ display: "flex", flexDirection: "column", gap: "30px" }}
        >
          <FormControl isInvalid={errors.name}>
            <Input
              id="name"
              placeholder="username/email"
              {...register("name", {
                required: "This is required",
                minLength: { value: 1, message: "Minimum length should be 1" },
              })}
              borderColor="black"
              _hover={{ borderColor: "grey" }}
            />
            <FormErrorMessage>
              {errors.name && errors.name.message}
            </FormErrorMessage>
          </FormControl>
          <FormControl isInvalid={errors.password}>
            <Input
              type="password"
              id="password"
              placeholder="password"
              {...register("password", {
                required: "This is required",
                minLength: { value: 1, message: "Minimum length should be 1" },
              })}
              borderColor="black"
              _hover={{ borderColor: "grey" }}
            />
            <FormErrorMessage>
              {errors.password && errors.password.message}
            </FormErrorMessage>
          </FormControl>
          <Button
            colorScheme="teal"
            isLoading={isSubmitting}
            type="submit"
            bg="brand.purple"
            _hover={{ bg: "purple.700" }}
            color="white"
            paddingX="25px"
            w="150px"
            alignSelf="center"
          >
            Submit
          </Button>
        </form>
      </Flex>
    </Container>
  );
};
