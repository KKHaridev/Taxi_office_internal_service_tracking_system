import { Box, Input, Heading, Flex, Select, Button } from "@chakra-ui/react";
import { useState } from "react";

export const InputField = ({ label, width, value, status, select }) => {
  return (
    <>
      <Box w={width ? width : "400px"}>
        {label && <label htmlFor="">{label}</label>}
        {select ? (
          <Select id="" name="" mt="5px" size="md" textTransform={"capitalize"}>
            <option value="none" selected disabled hidden>
              {value}
            </option>
            <option value="Waiting">Waiting</option>
            <option value="In-Progress">In-Progress</option>
            <option value="Arrived">Arrived</option>
            <option value="Delayed By User">Delayed By User</option>
            <option value="Taxi Malfunction">Taxi Malfunction</option>
            <option value="Delayed By User">Delayed By User</option>
          </Select>
        ) : (
          <Input id="" name="" mt="5px" isDisabled={status} value={value} />
        )}
      </Box>
    </>
  );
};

export const Doulbe = ({ children }) => {
  return (
    <Flex
      w="100%"
      gap={{ base: "25px", md: "40px" }}
      flexDirection={{ base: "column", md: "row" }}
      alignItems="center"
    >
      {children}
    </Flex>
  );
};

export const DateComponent = ({ label, width, value, status, select }) => {
  const [date,setDate]=useState(value);
  return (
    <>

      <Box w={width ? width : "400px"}>
        {label && <label htmlFor="">{label}</label>}
        <Input
          id=""
          name=""
          mt="5px"
          placeholder="Select Date and Time"
          size="md"
          type="date"
          value={date}
          onChange={(e)=>setDate(e.target.value)}
        />
      </Box>
    </>
  );
};
