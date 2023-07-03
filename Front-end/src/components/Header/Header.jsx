import React from "react";
import {
  Container,
  Heading,
  Spacer,
  Stack,
  Avatar,
  Popover,
  PopoverTrigger,
  PopoverContent,
  PopoverBody,
  Text,
  Button,
  Link,
} from "@chakra-ui/react";
import { VscBellDot } from "react-icons/vsc";
import { Link as _Link } from "react-router-dom";
import { useAuth } from "@context/AuthContext";
import { useLocation } from "react-router-dom";

export const Header = () => {
  const auth = useAuth();
  const location = useLocation();
  const admin = location.pathname.includes("admin");
  return (
    <Container
      as="header"
      maxW="100%"
      py={5}
      px="2%"
      h="60px"
      display="flex"
      alignItems="center"
      justifyContent="center"
      borderBottom="1px solid #808080"
    >
      <Heading
        as="h4"
        fontSize={["22px"]}
        color="brand.yellow"
        fontWeight="500"
      >
        LOGO/BRAND
      </Heading>
      <Spacer />
      <Stack direction="row" alignItems="center">
        <VscBellDot fontSize="1.2rem" />
        <Text fontSize="md" px="20px" cursor="pointer">
          Hello {auth?.user?.username}
        </Text>
        <Popover>
          <PopoverTrigger>
            <Avatar
              size="sm"
              src="https://bit.ly/broken-link"
              bg="brand.yellow"
              cursor="pointer"
            />
          </PopoverTrigger>
          <PopoverContent
            w="200px"
            mr="50px"
            py="15px"
            _focusVisible={{ outline: "none" }}
          >
            <PopoverBody
              display="flex"
              flexDir="column"
              gap="15px"
              alignItems="center"
              justifyContent="center"
            >
              {admin ? (
                ""
              ) : (
                <Link
                  as={_Link}
                  w="90%"
                  display="flex"
                  alignItems="center"
                  justifyContent="center"
                  to="/profile"
                >
                  Profile
                </Link>
              )}
              <Button
                bg="brand.purple"
                _hover={{ bg: "purple.700" }}
                color="white"
                paddingX="25px"
                h="35px"
                fontSize="16px"
                onClick={() => {
                  auth.logout();
                }}
              >
                Log Out
              </Button>
            </PopoverBody>
          </PopoverContent>
        </Popover>
      </Stack>
    </Container>
  );
};
