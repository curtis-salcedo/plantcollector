import React, { useState } from 'react';

// Styles
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

export default function NavBar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <Navbar color="success" dark fixed>
      <Nav>
    <NavbarBrand href="/">
      <img
        alt="logo"
        src="https://i.imgur.com/cMijoSws.png"
        style={{
          height: 40,
          width: 40
        }}
      />
      Reactstrap
    </NavbarBrand>
      <NavItem nav>
        <NavLink href="/" nav>Link 1</NavLink>
      </NavItem>

    </Nav>
  </Navbar>
  );
}