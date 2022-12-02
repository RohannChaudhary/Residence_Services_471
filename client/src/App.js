import Login from "./components/HomePage/Login";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import StudentDashboard from "./components/StudentDashboard";
import StudentMaintenance from "./components/StudentMaintenance";
import StudentComplaints from "./components/StudentComplaints";
import AdminDashboard from "./components/AdminDashboard";
import AdminComplaints from "./components/AdminComplaints";
import TechDashboard from "./components/TechDashboard";
import TechMaintenance from "./components/TechMaintenance";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login />,
    },
    {
      path: "/studentdashboard",
      element: <StudentDashboard />,
    },
    {
      path: "/studentdashboard/Maintenance",
      element: <StudentMaintenance />,
    },
    {
      path: "/studentdashboard/complaints",
      element: <StudentComplaints />,
    },
    {
      path: "/admindashboard",
      element: <AdminDashboard />,
    },
    {
      path: "/admindashboard/complaints",
      element: <AdminComplaints />,
    },
    {
      path: "/techdashboard",
      element: <TechDashboard />,
    },
    {
      path: "/techdashboard/maintenance",
      element: <TechMaintenance />,
    },
  ]);
  return (
    <>
      <RouterProvider router = {router}/>
    </>
  );
}

export default App;
