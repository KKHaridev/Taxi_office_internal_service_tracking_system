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
import { Doulbe } from "@components/InputComponents";

export const Label = ({ name }) => {
  return <label>{name}</label>;
};

export const SignUp3 = ({ submit, errors, register, isSubmitting, watch }) => {
  return (
    <form
      w={100}
      onSubmit={submit}
      style={{ display: "flex", flexDirection: "column", gap: "30px" }}
    >
      <Heading
        as="h5"
        fontSize={"16px"}
        fontWeight="500"
        color={"brand.purple"}
        textAlign={"center"}
        mb={3}
      >
        Please Fill Up The Following Taxi Details
      </Heading>
      <Doulbe>
        <FormControl isInvalid={errors.taxi_number}>
          <Label name="Taxi Number" />
          <Input
            id="taxi_number"
            {...register("taxi_number", {
              required: "This is required",
              minLength: {
                value: 1,
              },
            })}
            borderColor={errors?.taxi_number ? "red" : "gray"}
            _hover={{
              borderColor: errors?.taxi_number ? "red" : "gray",
            }}
            _focus={{
              borderColor: errors?.taxi_number ? "red" : "auto",
            }}
          />
        </FormControl>
        <FormControl isInvalid={errors.dob}>
          <Label name="Date Of Birth" />
          <Input
            type="date"
            id="dob"
            {...register("dob", {
              required: "This is required",
            })}
            borderColor={errors?.dob ? "red" : "gray"}
            _hover={{
              borderColor: errors?.dob ? "red" : "gray",
            }}
            _focus={{
              borderColor: errors?.dob ? "red" : "auto",
            }}
          />
        </FormControl>
      </Doulbe>

      <Doulbe>
        <FormControl isInvalid={errors.phone}>
          <Label name="Phone" />
          <Input
            id="phone"
            {...register("phone", {
              required: "This is required",
              minLength: {
                value: 1,
              },
            })}
            borderColor="gray"
            _hover={{ borderColor: "grey" }}
          />
        </FormControl>
        <FormControl isInvalid={errors.upi}>
          <Label name="UPI" />
          <Input
            type="text"
            id="upi"
            {...register("upi", {
              required: "This is required",
            })}
            borderColor="gray"
            _hover={{ borderColor: "grey" }}
          />
        </FormControl>
      </Doulbe>

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
        Next
      </Button>
    </form>
  );
};
