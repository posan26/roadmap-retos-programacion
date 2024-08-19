/* you need install package readline-sync */
import { writeFile, readFile, unlink } from "fs";
import readline from "readline-sync";

/* -- exercise */
const createFile = (fileName, content) => {
  writeFile(fileName, content, (err) => {
    if (err) {
      console.error("Error writing file:", err);
      return;
    }
    console.log("File created successfully!");
  });
};

const readFileContent = (fileName) => {
  readFile(fileName, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading file:", err);
      return;
    }
    console.log("File content:", data);
  });
};

const deleteFile = (fileName) => {
  unlink(fileName, (err) => {
    if (err) {
      console.error("Error deleting file:", err);
      return;
    }
    console.log("File deleted successfully!");
  });
};

const githubUsername = "qwik-zgheib";

const content = `Name: Qwik Zgheib\nAge: 22\nFavorite Programming Language: JavaScript`;

const fileName = `${githubUsername}.txt`;

createFile(fileName, content);
readFileContent(fileName);
deleteFile(fileName);

/* -- extra challenge */
import fs from "fs";
import path from "path";

const filePath = path.join(process.cwd(), "sales.txt");

const SalesManager = {
  addProduct: () => {
    const name = readline.question("Enter product name: ");
    const quantity = readline.questionInt("Enter quantity sold: ");
    const price = readline.questionFloat("Enter price: ");

    const productLine = `${name}, ${quantity}, ${price}\n`;
    fs.appendFileSync(filePath, productLine);
    console.log("Product added.");
  },

  viewProducts: () => {
    if (!fs.existsSync(filePath)) {
      console.log("No products found.");
      return;
    }
    const data = fs.readFileSync(filePath, "utf8");
    console.log("Current Products:\n" + data);
  },

  updateProduct: () => {
    if (!fs.existsSync(filePath)) {
      console.log("No products to update.");
      return;
    }
    const data = fs.readFileSync(filePath, "utf8");
    const products = data.split("\n").filter((line) => line.trim() !== "");
    const name = readline.question("Enter product name to update: ");

    const productIndex = products.findIndex((line) => line.split(", ")[0] === name);
    if (productIndex !== -1) {
      const quantity = readline.questionInt("Enter new quantity sold: ");
      const price = readline.questionFloat("Enter new price: ");
      products[productIndex] = `${name}, ${quantity}, ${price}`;
      fs.writeFileSync(filePath, products.join("\n") + "\n");
      console.log("Product updated.");
    } else {
      console.log("Product not found.");
    }
  },

  deleteProduct: () => {
    if (!fs.existsSync(filePath)) {
      console.log("No products to delete.");
      return;
    }
    const data = fs.readFileSync(filePath, "utf8");
    const products = data.split("\n").filter((line) => line.trim() !== "");
    const name = readline.question("Enter product name to delete: ");

    const newProducts = products.filter((line) => line.split(", ")[0] !== name);
    fs.writeFileSync(filePath, newProducts.join("\n") + "\n");
    console.log("Product deleted.");
  },

  calculateTotalSales: () => {
    if (!fs.existsSync(filePath)) {
      console.log("No sales data found.");
      return;
    }
    const data = fs.readFileSync(filePath, "utf8");
    const products = data.split("\n").filter((line) => line.trim() !== "");

    let totalSales = 0;
    products.forEach((line) => {
      const [, quantity, price] = line.split(", ");
      totalSales += parseInt(quantity) * parseFloat(price);
    });
    console.log("Total Sales: $" + totalSales.toFixed(2));
  },

  calculateSalesByProduct: () => {
    if (!fs.existsSync(filePath)) {
      console.log("No sales data found.");
      return;
    }
    const data = fs.readFileSync(filePath, "utf8");
    const products = data.split("\n").filter((line) => line.trim() !== "");

    const salesByProduct = {};
    products.forEach((line) => {
      const [name, quantity, price] = line.split(", ");
      if (!salesByProduct[name]) {
        salesByProduct[name] = 0;
      }
      salesByProduct[name] += parseInt(quantity) * parseFloat(price);
    });

    for (const [name, total] of Object.entries(salesByProduct)) {
      console.log(`${name}: $${total.toFixed(2)}`);
    }
  },

  exit: () => {
    if (fs.existsSync(filePath)) {
      fs.unlinkSync(filePath);
    }
    console.log("Exiting and deleting sales file.");
    process.exit();
  },
};

const mainMenu = () => {
  while (true) {
    console.log(
      "\n1. Add Product\n2. View Products\n3. Update Product\n4. Delete Product\n5. Calculate Total Sales\n6. Calculate Sales by Product\n7. Exit"
    );

    let choice = readline.questionInt("Enter your choice: ");

    while (choice < 1 || choice > 7) {
      console.log("Invalid choice. Please try again.");
      choice = readline.questionInt("Enter your choice: ");
    }
    if (choice === 1) SalesManager.addProduct();
    if (choice === 2) SalesManager.viewProducts();
    if (choice === 3) SalesManager.updateProduct();
    if (choice === 4) SalesManager.deleteProduct();
    if (choice === 5) SalesManager.calculateTotalSales();
    if (choice === 6) SalesManager.calculateSalesByProduct();
    if (choice === 7) SalesManager.exit();
  }
};

mainMenu();
