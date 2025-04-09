import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

const Navbar = () => {
  const { cartItems } = useCart();

  const cartCount = cartItems.reduce((total, item) => total + item.quantity, 0);

  return (
    <nav style={styles.navbar}>
      <Link to="/products" style={styles.link}>Products</Link>
      <Link to="/cart" style={styles.link}>
        Cart 🛒 {cartCount > 0 && <span style={styles.badge}>{cartCount}</span>}
      </Link>
      <Link to="/orders" style={styles.link}>Orders</Link>
      <Link to="/dashboard" style={styles.link}>Dashboard</Link>
      <Link to="/login" style={styles.link}>Login</Link>
    </nav>
  );
};

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-around",
    padding: "10px",
    background: "#eee",
  },
  link: {
    textDecoration: "none",
    fontWeight: "bold",
    color: "#333",
    position: "relative",
  },
  badge: {
    background: "red",
    color: "white",
    borderRadius: "50%",
    padding: "2px 6px",
    marginLeft: "5px",
    fontSize: "0.8rem",
  },
};

export default Navbar;
