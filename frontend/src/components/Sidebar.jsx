import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-router-dom';

const Sidebar = () => {
  return (
    <div className="sidebar bg-dark text-white d-flex flex-column p-3 vh-100">
      <h4 className="text-white text-center mb-4 mt-3 d-none d-md-block">APRA</h4>
      
      <Nav className="flex-column w-100">
        <Nav.Link
          as={NavLink}
          to="/"
          end
          className="nav-link text-white text-start mb-2"
        >
          <i className="bi bi-house-door-fill pe-2"></i>
          <span className="d-none d-md-inline">Home</span>
        </Nav.Link>
        <Nav.Link
          as={NavLink}
          to="/analyze"
          className="nav-link text-white text-start mb-2"
        >
          <i className="bi bi-chat-text-fill pe-2"></i>
          <span className="d-none d-md-inline">Analyze</span>
        </Nav.Link>
        <Nav.Link
          as={NavLink}
          to="/train"
          className="nav-link text-white text-start mb-2"
        >
          <i className="bi bi-wrench-adjustable pe-2"></i>
          <span className="d-none d-md-inline">Train</span>
        </Nav.Link>
      </Nav>

      <div className="mt-auto text-white text-start p-3 w-100">
        <i className="bi bi-person-circle pe-2 fs-5"></i>
        <span className="d-none d-md-inline">User</span>
      </div>
    </div>
  );
};

export default Sidebar;