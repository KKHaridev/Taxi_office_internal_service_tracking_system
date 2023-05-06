import React from "react";
import { useTable } from "react-table";
import { Table as TableC, Thead, Tbody, Tr, Th, Td } from "@chakra-ui/react";

export const Table = ({ columns, data }) => {
  const tableInstance = useTable({
    columns,
    data,
  });

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    tableInstance;

  return (
    <TableC {...getTableProps()} sx={{ borderCollapse: 'separate', borderSpacing: '0 10px', }}>
      <Thead>
        {headerGroups.map((headerGroup) => {
          const { key, ...restHeaderGroupProps } =
            headerGroup.getHeaderGroupProps();
          return (
            <Tr key={key} {...restHeaderGroupProps}>
              {headerGroup.headers.map((column) => {
                const { key, ...columnProps } = column.getHeaderProps();
                return (
                  <Th
                    key={key}
                    {...columnProps}
                    bg="brand.purple"
                    color="white"
                    h="50px"
                  >
                    {column.render("Header")}
                  </Th>
                );
              })}
            </Tr>
          );
        })}
      </Thead>
      <Tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          const { key, ...restRowProps } = row.getRowProps();
          return (
            <Tr key={key} {...restRowProps}>
              {row.cells.map((cell) => {
                const { key, ...restCellProps } = cell.getCellProps();
                return (
                  <Td key={key} {...restCellProps}>
                    {cell.render("Cell")}
                  </Td>
                );
              })}
            </Tr>
          );
        })}
      </Tbody>
    </TableC>
  );
};
