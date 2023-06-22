import React from "react";
import { Breadcrumb } from "../components/Breadcrumb";
import { Table } from "@components/Table";
import { useNavigate } from "react-router-dom";
import { useDelete, useUpdateStatus, useData } from "../hooks/useData";
import { TableHolder } from "../components/TableHolder/TableHolder";

import { Modal } from "../components/Modals/Modal";
import { CloseIcon, DeleteIcon } from "@chakra-ui/icons";
import { useDisclosure } from "@chakra-ui/react";
import { BiToggleLeft, BiToggleRight } from "react-icons/bi";

const ViewButton = ({ row }) => {
  const navigate = useNavigate();

  const id = row.values.id;
  return (
    <button onClick={() => navigate(`/admin/cars_and_drivers/${id}`)}>View</button>
  );
};

const Disable_Enable = ({ row }) => {
  const id = row.values.id;
  const availability = row.values.availability;
  const status = row.values.status;
  const { mutate: updateStatus } = useUpdateStatus();

  return (
    <>
      <Modal
        title="Accept"
        color="#EA0000"
        hColor="#FB4C4C"
        handler={() => {
          const data = { status: status == "active" ? "disabled" : "active" };
          updateStatus({ id, data });
        }}
        disable={availability == "In Ride" ? true : false}
      >
        {status == "disabled" ? <BiToggleLeft size={25} /> : <BiToggleRight color="brand.green" size={25} />}
      </Modal>
    </>
  );
};

const DeleteUser = ({ row }) => {
  const id = row.values.id;
  const availability = row.values.availability;
  const { onClose } = useDisclosure();
  const { mutate: deleteUser } = useDelete();

  return (
    <>
      <Modal
        title="Confirm Rejection"
        color="#6E2594"
        hColor="#8344a5"
        handler={() => {
          deleteUser({ id });
          onClose();
        }}
        disable={availability == "In Ride" ? true : false}
      >
        <DeleteIcon color="brand.red" />
      </Modal>
    </>
  );
};
const COLUMNS = [
  {
    Header: "Driver ID",
    accessor: "id",
  },
  {
    Header: "Driver Name",
    accessor: "username",
  },
  {
    Header: "Taxi Number",
    accessor: "taxi_details.taxi_no",
  },
  {
    Header: "Total Rides",
    accessor: "total_rides",
  },
  {
    Header: "Current Status",
    accessor: "availability",
  },
  {
    Header: "Disable/Enable",
    accessor: "status",
    Cell: Disable_Enable,
  },
  {
    Header: "Delete",
    accessor: "delete",
    Cell: DeleteUser,
  },
  {
    Header: "Earnings",
    accessor: (data) => <>&#8377; {data.earnings.total_earnings}</>,
  },
  {
    Header: "View",
    accessor: "view",
    Cell: ViewButton,
  },
];

export const CarsAndDrivers = () => {
  const { isLoading, error, data } = useData("driverDetails", "drivers", {
    refetchInterval: 1000,
  });

  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;

  return (
    <div>
      <Breadcrumb />
      <TableHolder>
        <Table columns={COLUMNS} data={data} />
      </TableHolder>
    </div>
  );
};
