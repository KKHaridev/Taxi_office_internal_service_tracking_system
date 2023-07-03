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

  const id = row.values.driver_id;
  return (
    <button onClick={() => navigate(`/admin/cars_and_drivers/${id}`)}>
      View
    </button>
  );
};

const Disable_Enable = ({ row }) => {
  const id = row.values.driver_id;
  const availability = row.values.availability;
  const status = row.values.driver_status;
  const { mutate: updateStatus } = useUpdateStatus();

  return (
    <>
      <Modal
        title="Accept"
        color="#EA0000"
        hColor="#FB4C4C"
        handler={() => {
          const data = { action: status == "available" ? "disable" : "enable" };
          let endpoint = `api/admin/drivers/${id}/delete-or-disable/`;
          updateStatus({ id, data, endpoint });
        }}
      >
        {status == "unavailable" ? (
          <BiToggleLeft size={25} />
        ) : (
          <BiToggleRight color="brand.green" size={25} />
        )}
      </Modal>
    </>
  );
};

const DeleteUser = ({ row }) => {
  const id = row.values.driver_id;
  const availability = row.values.driver_status;
  const { onClose } = useDisclosure();
  const { mutate: updateStatus } = useUpdateStatus();


  return (
    <>
      <Modal
        title="Confirm Rejection"
        color="#6E2594"
        hColor="#8344a5"
        let
        endpoint=""
        handler={() => {
          const data = { action: "delete" };
          let endpoint = `api/admin/drivers/${id}/delete-or-disable/`;
          updateStatus({ id, data, endpoint });
        }}
        disable={availability == "available" ? true : false}
      >
        <DeleteIcon color="brand.red" />
      </Modal>
    </>
  );
};
const COLUMNS = [
  {
    Header: "Driver ID",
    accessor: "driver_id",
  },
  {
    Header: "Driver Name",
    accessor: "driver_name",
  },
  {
    Header: "Taxi Number",
    accessor: "taxi_num",
  },
  {
    Header: "Total Rides",
    accessor: "total_rides",
  },
  {
    Header: "Current Status",
    accessor: "driver_status",
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
    accessor: (data) => <>&#8377; {data?.total_earning}</>,
  },
  {
    Header: "View",
    accessor: "view",
    Cell: ViewButton,
  },
];

export const CarsAndDrivers = () => {
  const { isLoading, error, data, isSuccess } = useData(
    "driver_Details",
    "api/admin/drivers/list/",
    { refetchInterval: 1000 }
  );
  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  if (isSuccess) console.log(data);
  return (
    <div>
      <Breadcrumb />
      <TableHolder>
        <Table columns={COLUMNS} data={data?.drivers} />
      </TableHolder>
    </div>
  );
};
