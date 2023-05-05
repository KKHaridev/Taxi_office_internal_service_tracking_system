import React from "react";
import {
  Breadcrumb as BreadCrumb,
  BreadcrumbItem,
  BreadcrumbLink,
} from "@chakra-ui/react";
import { ChevronRightIcon } from "@chakra-ui/icons";
import { useLocation } from "react-router-dom";

export const Breadcrumb = () => {
  const location = useLocation();
  const locations = location.pathname.split("/").splice(1);
  return (
    <BreadCrumb spacing="8px" separator={<ChevronRightIcon color="gray.500" />}>
      <BreadcrumbItem isCurrentPage={location.pathname == "/"}>
        <BreadcrumbLink href="/">Home</BreadcrumbLink>
      </BreadcrumbItem>
      {locations.map((location, index) => (
        <BreadcrumbItem
          key={index}
          isCurrentPage={index === locations.length - 1}
        >
          <BreadcrumbLink href={location}>{location}</BreadcrumbLink>
        </BreadcrumbItem>
      ))}
    </BreadCrumb>
  );
};
