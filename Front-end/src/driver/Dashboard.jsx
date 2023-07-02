import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { CardHolder } from "@components/Card/CardHolder";
import { useAuth } from "@context/AuthContext";
import { BsCurrencyDollar } from "react-icons/bs";
import { RiUserReceived2Fill } from "react-icons/ri";
import { useData } from "../hooks/useData";
import { Text, Flex, Grid } from "@chakra-ui/react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const optionsearning = {
  responsive: true,
  scales: {
    y: {
      min: 0,
      ticks: {
        stepSize: 100,
      },
    },
  },
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Past 4 Days Earnings",
    },
  },
};

export const optionsride = {
  responsive: true,
  scales: {
    y: {
      min: 0,
      ticks: {
        stepSize: 100,
      },
    },
  },
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Past 4 Days Rides",
    },
  },
};

export const Dashboard = () => {
  const { isLoading, error, data, isSuccess } = useData(
    "dashboard",
    `api/dashboard`
  );

  if (isLoading) {
    return (
      <>
        <Breadcrumb />
        <Text mt={6}>Loading</Text>
      </>
    );
  }
  console.log(data);
  if (error) {

    return (
      <>
        <Breadcrumb />
        <Text mt={6}>No Data Available</Text>
      </>
    );
  }

  if (isSuccess) {
    const cardData = [
      {
        icon: BsCurrencyDollar,
        title: "Earnings",
        number: `&#8377; ${data?.total_earnings}`,
      },

      {
        icon: RiUserReceived2Fill,
        title: "Received_Rides",
        number: `${data?.total_rides}`,
      },
    ];
    const earnings = {
      labels: Object.values(data?.daily_totals).map(
        (item, index) => item?.date
      ),
      datasets: [
        {
          label: "Earings",
          data: Object.values(data?.daily_totals).map(
            (item, index) => item?.total_earnings
          ),
          backgroundColor: ["#D2FF28", "#C84C09", "#5C80BC", "#FF8811"],
        },
      ],
    };
    const rides = {
      labels: Object.values(data?.daily_totals).map((item, index) => item.date),
      datasets: [
        {
          label: "Rides",
          data: Object.values(data?.daily_totals).map(
            (item, index) => item.total_rides
          ),
          backgroundColor: ["#5C80BC", "#D2FF28", "#C84C09", "#FF8811"],
        },
      ],
    };
    return (
      <>
        <Breadcrumb />
        <Grid
          overflowY={"scroll"}
          w="90vw"
          height={"calc(100vh - 180px)"}
          gridTemplateColumns="repeat(4,1fr)"
          gridTemplateRows={"repeat(4,1fr)"}
          paddingBottom={2}
        >
          <CardHolder cardData={cardData} />
          <Flex
            w={700}
            marginLeft={{ base: "0", md: "30px" }}
            alignItems="center"
            justifyContent="center"
            flexDir="column"
            gap="15px"
            bg="white"
            borderRadius="7px"
            boxShadow="0px 4px 4px rgba(0, 0, 0, 0.25)"
            padding={4}
            gridColumn={"3/5"}
            gridRow={"1/5"}
          >
            <Line options={optionsearning} data={earnings} />
            <Line options={optionsride} data={rides} />
          </Flex>
          <Flex gridColumn="1/3" gridRow="3/5">
            <img
              src="https://www.smcrealty.com/images/microsites/location-map/mantri-serenity-251.jpg"
              alt="img"
            />
          </Flex>
        </Grid>
      </>
    );
  }
};
