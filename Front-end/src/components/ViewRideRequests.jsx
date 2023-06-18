import React from "react";
import { Breadcrumb } from "./Breadcrumb";
import { useParams } from "react-router-dom";
import { useData } from "../hooks/useData";
import { Box, Input, Heading, Flex, Select, Button } from "@chakra-ui/react";
import { InputField } from "./InputComponents";

export const ViewRideRequests = () => {
  let { id } = useParams();
  const { isLoading, error, data } = useData(
    "ride data",
    `req_rides/${id}`,
    null,
    null,
    { refetchInterval: 0 }
  );
  console.log(data);
  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  return (
    <>
      <Breadcrumb />
      <Box mt="20px" height={"100%"}>
        <Heading as="h3" size="md">
          Details
        </Heading>
        <Flex
          gap="20px"
          maxW="1024px"
          mt="10px"
          direction={"column"}
          overflowY={"auto"}
          height={"80%"}
        >
          <Flex
            w="100%"
            gap="40px"
            flexDirection={{ base: "column", md: "row" }}
          >
            <InputField label="ID" width="90%" status={true} value={data.id} />
            <InputField
              label="Passenger"
              width="90%"
              status={true}
              value={data.pass_name}
            />
          </Flex>
          <Flex
            w="100%"
            gap="40px"
            flexDirection={{ base: "column", md: "row" }}
          >
            <InputField
              label="From"
              width="90%"
              status={true}
              value={data.from}
            />
            <InputField label="To" width="90%" status={true} value={data.to} />
          </Flex>
          <Flex
            w="100%"
            gap="40px"
            flexDirection={{ base: "column", md: "row" }}
          >
            <InputField
              label="Start Time"
              width="90%"
              status={true}
              value={data.start_time}
            />
            <InputField
              label="Expected Time"
              width="90%"
              status={true}
              value={data.expected_time}
            />
          </Flex>
          <Flex
            w="100%"
            gap="40px"
            flexDirection={{ base: "column", md: "row" }}
          >
            <InputField
              label="Status"
              width="90%"
              status={false}
              value={data.status}
              select={true}
            />
            <InputField
              label="Interested in car pooled rides"
              width="90%"
              status={true}
              value={data.interested_in_car_pooled}
            />
          </Flex>
          <Flex
            w="100%"
            gap="40px"
            flexDirection={{ base: "column", md: "row" }}
          >
            <InputField
              label="Expected Driver Pay"
              width="90%"
              status={true}
              value={data.exp_amount}
            />
            <InputField
              label="Percentage of car pooled ride"
              width="90%"
              status={true}
              value={data.percentage}
            />
          </Flex>
        </Flex>
        <Button
          colorScheme="teal"
          type="submit"
          bg="brand.purple"
          _hover={{ bg: "purple.700" }}
          color="white"
          paddingX="25px"
          w="150px"
          alignSelf="center"
          mt={[9, 12]}
        >
          Submit
        </Button>
      </Box>
    </>
  );
};
