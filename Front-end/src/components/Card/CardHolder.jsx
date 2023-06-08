import React from "react";
import { Card } from "./Card";
import { Flex } from "@chakra-ui/react";

export const CardHolder = ({ cardData }) => {
  return (
    <Flex  gap={6} py="15px">
      {cardData.map((item, index) => (
        <Card icon={item.icon} title={item.title} number={item.number} key={index} />
      ))}
    </Flex>
  );
};
