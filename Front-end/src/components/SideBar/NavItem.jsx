import React from "react";
import { Link, Flex } from "@chakra-ui/react";
import { NavLink as _Link } from "react-router-dom";

export const NavItem = ({ icon, title, size, link, handler }) => {
  return (
    <Flex direction="column" p="0 10px">
      <Link
        as={_Link}
        transition="0.3s ease-in-out"
        to={link}
        display="flex"
        alignItems="center"
        justifyContent={!size && "center"}
        h={30}
        p="20px 5px"
        m="8px 0"
        borderRadius="md"
        color="black"
        fontSize=".9rem"
        border="1px solid transparent"
        _hover={{ borderColor: "black" }}
        onClick={handler}
      >
        <Flex alignItems="center" justifyContent="center" h="100%">
          <Flex m={size && "0 10px"} fontSize="1.2rem" transition="0.2s ease">
            {icon}
          </Flex>{" "}
          {size && title}
        </Flex>
      </Link>
    </Flex>
  );
};
