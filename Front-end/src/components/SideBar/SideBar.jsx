import { Box, Flex, Button, useBoolean, Spacer } from "@chakra-ui/react";
import React from "react";
import { ChevronLeftIcon, ChevronRightIcon, Icon } from "@chakra-ui/icons";
import {NavItem} from "@components";
import {
  AiOutlineHome,
  AiOutlineUser,
  AiOutlineBranches,
  AiOutlineShop,
} from "react-icons/ai";
import { FaProductHunt } from "react-icons/fa";
import { BiCategoryAlt } from "react-icons/bi";

export const SideBar = () => {
  //true ==> big
  const [size, setSize] = useBoolean(false);
  return (
    <Flex
      as="aside"
      zIndex={10}
      pos="absolute"
      direction="column"
      w={size ? 200 : "70px"}
      h="calc(100vh - 60px)"
      transition="0.2s ease"
      borderRight="1px solid var(--display-400)"
      top="60px"
      backgroundColor="#F5F5F5"
    >
      <Box pos="relative" top="20px">
        <NavItem
          icon={<Icon as={AiOutlineHome} />}
          title="test"
          size={size}
          link="/"
        />

        <NavItem
          icon={<Icon as={FaProductHunt} />}
          title="test"
          size={size}
          link="test"
        />

        <NavItem
          icon={<Icon as={AiOutlineUser} />}
          title="test"
          size={size}
          link="test"
        />
        <NavItem
          icon={<Icon as={AiOutlineShop} />}
          title="test"
          size={size}
          link="test"
        />
        <NavItem
          icon={<Icon as={AiOutlineBranches} />}
          title="test"
          size={size}
          link="test"
        />
        <NavItem
          icon={<Icon as={BiCategoryAlt} />}
          title="test"
          size={size}
          link="test"
        />
      </Box>
      <Spacer />
      <Box p="10px" pos="relative" bottom="0" transition={"0.2s ease"}>
        <Button
          onClick={setSize.toggle}
          w="100%"
          position="relative"
          bottom="10px"
          bg="brand.purple"
          _hover={{ bg: "purple.700" }}
          color="white"
        >
          {size ? <ChevronLeftIcon /> : <ChevronRightIcon />}
        </Button>
      </Box>
    </Flex>
  );
};
