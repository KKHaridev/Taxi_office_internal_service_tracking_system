import React from "react";
import {
  Breadcrumb as BreadCrumb,
  BreadcrumbItem,
  BreadcrumbLink,
} from "@chakra-ui/react";
import { ChevronRightIcon } from "@chakra-ui/icons";
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

export const Breadcrumb = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const admin = location.pathname.includes("admin");
  const locations = admin
    ? location.pathname.split("/").splice(2)
    : location.pathname.split("/").splice(1);

  return (
    <BreadCrumb spacing="8px" separator={<ChevronRightIcon color="gray.500" />}>
      <BreadcrumbItem isCurrentPage={location.pathname == "/"}>
        <BreadcrumbLink href={admin ? "/admin" : "/"}>Home</BreadcrumbLink>
      </BreadcrumbItem>
      {locations.map((location, index) => (
        <BreadcrumbItem
          key={index}
          isCurrentPage={index === locations.length - 1}
        >
          <BreadcrumbLink
            onClick={() => {
              navigate(-1);
            }}
            textTransform="capitalize"
          >
            {location.replace("_", " ")}
          </BreadcrumbLink>
        </BreadcrumbItem>
      ))}
    </BreadCrumb>
  );
};
