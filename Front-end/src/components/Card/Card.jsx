import React from "react";
import { Flex, Heading, Text } from "@chakra-ui/react";
import { Link } from "react-router-dom";
export const Card = ({ title, number }) => {
  return (
    <Link to={title.toLowerCase()}>
      <Flex
        alignItems="center"
        justifyContent="center"
        flexDir="column"
        gap="15px"
        minW="300px"
        height={["100px", "125px"]}
        bg="white"
        borderRadius="7px"
      >
        <Heading as="h4" size="md">
          {title}
        </Heading>
          
        <Text dangerouslySetInnerHTML={{ __html: number }}></Text>
      </Flex>
    </Link>
  );
};
