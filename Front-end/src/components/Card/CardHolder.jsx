import React from "react";
import { Card } from "./Card";
import { SimpleGrid } from "@chakra-ui/react";

export const CardHolder = ({ cardData }) => {
  return (
    <SimpleGrid
      gridTemplateColumns={{ base: "repeat(1,300px)", md: "repeat(2,300px)" }}
      gridColumn="1/3"
      gridRow="1/3"
      justifyContent="center"
      alignContent="center"
      gap={6}
      py="15px"
    >
      {cardData.map((item, index) => (
        <Card
          icon={item.icon}
          title={item.title}
          number={item.number}
          key={index}
        />
      ))}
    </SimpleGrid>
  );
};
2