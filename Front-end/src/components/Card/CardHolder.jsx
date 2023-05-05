import React from "react";
import { Card } from "./Card";
import { SimpleGrid } from "@chakra-ui/react";

export const CardHolder = ({ cardData }) => {
  return (
    <SimpleGrid minChildWidth="270px" gap={6} py="15px">
      {cardData.map((item, index) => (
        <Card title={item.title} number={item.number} key={index} />
      ))}
    </SimpleGrid>
  );
};
