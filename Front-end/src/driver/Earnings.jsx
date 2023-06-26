import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { Flex, Heading, Stack, Text } from "@chakra-ui/react";
import { useAuth } from "@context/AuthContext";
import { useData1 } from "../hooks/useData";

const Row = ({ heading, count, price }) => {
  return (
    <Flex justifyContent="space-between" alignItems="center" w="95%">
      <Heading as="h5" size="sm" textTransform="capitalize">
        {heading.replace("_", " ")}
      </Heading>
      <Text>{price ? <>&#8377;{count}</> : count}</Text>
    </Flex>
  );
};

export const Earnings = () => {
  const { user } = useAuth();
  const id = user?.driver_id;

  const { isLoading, error, data } = useData1(
    "earnings",
    `api/${user?.driver_id}/earnings`
  );
  if (isLoading) {
    return <h1>Loading</h1>;
  }
  console.log(data);

  return (
    <>
      <Breadcrumb />
      <Flex
        bg="white"
        w="320px"
        h="300px"
        mt="5px"
        justifyContent="center"
        alignItems="center"
        borderRadius="md"
        flexDir="column"
        gap="20px"
        p="15px"
      >
        <Heading
          as="h3"
          fontSize={["25px"]}
          fontWeight="light"
          color="brand.purple"
        >
          Earnings
        </Heading>
        <Flex direction="column" gap="24px" w="90%" alignItems="center">
          <Row heading="Total Rides" count={data.total_rides} />

          {Object.entries(data).map(([heading, count]) =>
            heading === "total_rides" ? (
              ""
            ) : (
              <Row heading={heading} count={[count]} price={true} />
            )
          )}
        </Flex>
      </Flex>
    </>
  );
};
