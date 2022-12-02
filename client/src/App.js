import Login from "./components/HomePage/Login";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import Fairy from "./components/Fairy";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login />,
    },
    {
      path: "/Fairy",
      element: <Fairy />,
    },
  ]);
  return (
    <>
      <RouterProvider router = {router}/>
    </>
  );
}

export default App;
