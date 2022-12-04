import Login from "./components/HomePage/Login";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import StudentDashboard from "./components/StudentDashboard";
import StudentMaintenance from "./components/StudentMaintenance";
import StudentComplains from "./components/StudentComplains";
import AdminDashboard from "./components/AdminDashboard";
import AdminComplains from "./components/AdminComplains";
import TechDashboard from "./components/TechDashboard";
import TechMaintenance from "./components/TechMaintenance";

// import React from "react";
// import "./index.css";
// import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
// import PrivateRoute from "./utils/PrivateRoute";
// import { AuthProvider } from "./context/AuthContext";
// import Login from "./views/loginPage";
// import ProtectedPage from "./views/ProtectedPage";

// function App() {
//   return (
//     <Router>
//       <div className="flex flex-col min-h-screen overflow-hidden">
//         <AuthProvider>
//           <Switch>
//             <PrivateRoute component={ProtectedPage} path="/protected" exact />
//             <Route component={Login} path="/" />
//           </Switch>
//         </AuthProvider>
//       </div>
//     </Router>
//   );
// }

// export default App;

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
