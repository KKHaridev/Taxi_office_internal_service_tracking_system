import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { Table } from "@components/Table";
import { useNavigate } from "react-router-dom";
import { useData } from "@hooks/useData";
import { Box, Flex, Button, Text, Input } from "@chakra-ui/react";
import { InputField } from "@components/InputComponents";
import { Avatar } from "@chakra-ui/react";
import { Doulbe } from "@components/InputComponents";
import { DateComponent } from "../components/InputComponents";

export const Profile = () => {
  const { isLoading, error, data } = useData("personal_data", "drivers?id=1");

  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  console.log(data);

  return (
    <Box w="100%">
      <Breadcrumb />
      <Box
        w="100%"
        h="86vh"
        display="flex"
        justifyContent="center"
        py={3}
        overflowY="auto"
      >
        <Flex
          gap="20px"
          w="min(992px,100%)"
          mt="10px"
          direction={"column"}
          alignItems="center"
          pr={"10px"}
        >
          <Avatar
            size="2xl"
            // name={data[0]?.name}
            src="https://bit.ly/broken-link"
          />
          <Doulbe>
            <InputField
              label="ID"
              width="90%"
              status={true}
              value={data[0]?.id}
            />
            <InputField label="Name" width="90%" value={data[0]?.name} />
          </Doulbe>
          <Doulbe>
            <InputField label="Email" width="90%" value={data[0]?.email} />
            <InputField
              label="Taxi Number"
              width="90%"
              value={data[0]?.taxi_details.taxi_no}
            />
          </Doulbe>
          <Doulbe>
            <InputField label="UPI ID" width="90%" value={data[0]?.upi} />
            <InputField label="Phone" width="90%" value={data[0]?.phone} />
          </Doulbe>
          <Button
            colorScheme="teal"
            type="submit"
            bg="brand.purple"
            _hover={{ bg: "purple.700" }}
            color="white"
            paddingX="25px"
            w="150px"
            py="20px"
            alignSelf="end"
            marginRight={{ base: "22px", md: "0" }}
          >
            Update
          </Button>

          {/* Taxi Details */}
          <Text fontWeight="900">Taxi Details</Text>
          <Doulbe>
            <InputField
              label="Taxi Number"
              width="90%"
              value={data[0]?.taxi_details.taxi_no}
            />
            <DateComponent
              label="Test Date"
              width="90%"
              value={data[0]?.taxi_details.test_date}
            />
          </Doulbe>
          <Doulbe>
            <DateComponent
              label="Pollution Validity"
              width="90%"
              value={data[0]?.taxi_details.test_date}
            />
            <DateComponent
              label="Insurance"
              width="90%"
              value={data[0]?.taxi_details.insurance_val}
            />
          </Doulbe>
          <Button
            colorScheme="teal"
            type="submit"
            bg="brand.purple"
            _hover={{ bg: "purple.700" }}
            color="white"
            paddingX="25px"
            w="150px"
            py="20px"
            alignSelf="end"
            marginRight={{ base: "22px", md: "0" }}
          >
            Update
          </Button>

          {/* Password Details */}
          <Text fontWeight="900">Update Password</Text>
          <Doulbe>
            <Input type="password" label="New Password" width="90%"/>
            <Input type="password" label="Confirm Password" width="90%"/>
          </Doulbe>
          <Button
            colorScheme="teal"
            type="submit"
            bg="brand.purple"
            _hover={{ bg: "purple.700" }}
            color="white"
            paddingX="25px"
            w="150px"
            py="20px"
            alignSelf="end"
            marginRight={{ base: "22px", md: "0" }}
          >
            Update
          </Button>
        </Flex>
      </Box>
    </Box>
  );
};
