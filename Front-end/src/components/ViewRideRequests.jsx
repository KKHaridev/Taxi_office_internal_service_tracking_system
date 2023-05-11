import React from "react";
import { Breadcrumb } from "./Breadcrumb";
import { useParams } from "react-router-dom";
import { useData } from "../hooks/useData";
import { Box, Input, Heading, Flex } from "@chakra-ui/react";

export default function InputField({ label, width, value ,status}) {
  return (
    <>
      <Box w={width ? width : "400px"}>
        {label && <label htmlFor="">{label}</label>}
        <Input id="" name="" mt="5px" isDisabled={status} value={value}/>
      </Box>
    </>
  );
}

export const ViewRideRequests = () => {
  let { id } = useParams();
  const { isLoading, error, data } = useData("req", `req_rides/${id}`);
  console.log(data);
  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  return (
    <>
      <Breadcrumb />
      <Box mt="20px">
        <Heading as="h3" size="md">
          Details
        </Heading>
        <Flex gap="20px" maxW="1024px" mt="10px" flexDir="column">
          <Flex w="100%"  gap="40px">
            <InputField label="ID" width="90%" status={true} value={data.id}/>
            <InputField label="Passenger" width="90%" status={true} value={data.pass_name} />
          </Flex>
          <Flex w="100%"  gap="40px">
            <InputField label="From" width="90%" status={true} value={data.from}/>
            <InputField label="To" width="90%" status={true} value={data.to} />
          </Flex>
          <Flex w="100%"  gap="40px">
            <InputField label="Start Time" width="90%" status={true} value={data.start_time}/>
            <InputField label="Expected Time" width="90%" status={true} value={data.expected_time} />
          </Flex>
          <Flex w="100%"  gap="40px">
            <InputField label="Status" width="90%" status={false} value={data.id}/>
            <InputField label="Interested in car pooled rides" width="90%" status={true} value={data.interested_in_car_pooled} />
          </Flex>
          <Flex w="100%"  gap="40px">
            <InputField label="Expected Driver Pay" width="90%" status={true} value={data.exp_amount}/>
            <InputField label="Percentage of car pooled ride" width="90%" status={true} value={data.percentage} />
          </Flex>
        </Flex>
      </Box>
    </>
  );
};
