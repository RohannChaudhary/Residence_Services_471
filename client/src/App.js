import Login from "./components/HomePage/Login";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import StudentDashboard from "./components/StudentDashboard";
import StudentMaintenance from "./components/StudentMaintenance";
import StudentComplains from "./components/StudentComplains";
import AdminDashboard from "./components/AdminDashboard";
import AdminComplains from "./components/AdminComplains";
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
      path: "/studentdashboard/complains",
      element: <StudentComplains />,
    },
    {
      path: "/admindashboard",
      element: <AdminDashboard />,
    },
    {
      path: "/admindashboard/complains",
      element: <AdminComplains />,
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
