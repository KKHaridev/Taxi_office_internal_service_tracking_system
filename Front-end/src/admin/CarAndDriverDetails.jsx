import React from "react";
import { Breadcrumb } from "../components/Breadcrumb";
import { useParams } from "react-router-dom";
import { useData } from "../hooks/useData";
import { Box, Input, Heading, Flex, Select, Button } from "@chakra-ui/react";
import {
  DateComponent,
  Doulbe,
  InputField,
} from "../components/InputComponents";

export const CarsAndDriversDetails = () => {
  let { id } = useParams();
  const { isLoading, error, data } = useData("details", `drivers/${id}`);
  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  return (
    <>
      <Breadcrumb />
      <Box mt="20px" height={"100%"}>
        <Heading as="h3" size="sm">
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
          <Doulbe>
            <InputField
              label="Driver ID"
              width="90%"
              status={true}
              value={data.id}
            />
            <InputField label="Driver Name" width="90%" value={data.username} />
          </Doulbe>
          <Doulbe>
            <InputField
              label="Current Status"
              width="90%"
              value={data.availability}
            />
            <InputField label="Contact Number" width="90%" value={data.phone} />
          </Doulbe>
          <Doulbe>
            <InputField
              label="Total Earnings"
              width="90%"
              value={data.earnings.total_earnings}
            />
            <InputField label="UPI ID" width="90%" value={data.upi} />
          </Doulbe>
          <Heading as="h4" size="sm">
            Taxi Details
          </Heading>
          <Doulbe>
            <InputField
              label="Model"
              width="90%"
              value={data.taxi_details.car_model}
            />
            <InputField label="Type" width="90%" value={data.taxi_details.type} />
          </Doulbe>
          <Doulbe>
            <InputField
              label="Taxi Number"
              width="90%"
              value={data.taxi_details.taxi_no}
            />
            <DateComponent
              label="Test Date"
              width="90%"
              value={data.taxi_details.test_date}
              status={true}
            />
          </Doulbe>
          <Doulbe>
            <DateComponent
              label="Pollution Validity"
              width="90%"
              status={true}
              value={data.taxi_details.insurance_val}
            />
            <DateComponent
              label="Insurance"
              status={true}
              width="90%"
              value={data.taxi_details.insurance_val}
            />
          </Doulbe>
        </Flex>
      </Box>
    </>
  );
};
