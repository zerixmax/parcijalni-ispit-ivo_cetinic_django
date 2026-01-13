from django.contrib.auth.models import User
from products.models import Product
from offers.models import Offer, OfferItem
from customers.models import Customer
from decimal import Decimal
from random import randint, choice
from datetime import datetime, timedelta

def run():
    # List of product names and descriptions
    product_data = [
        {"name": "Wireless Keyboard", "description": "A sleek wireless keyboard with ergonomic design and long-lasting battery life. Perfect for work and gaming."},
        {"name": "Gaming Mouse", "description": "High-precision gaming mouse with customizable RGB lighting and adjustable DPI settings for ultimate control."},
        {"name": "Noise-Canceling Headphones", "description": "Over-ear headphones with active noise canceling and immersive sound quality for music and calls."},
        {"name": "Portable SSD", "description": "Ultra-fast portable SSD with 1TB storage capacity and USB-C connectivity. Ideal for data transfer on the go."},
        {"name": "4K Monitor", "description": "27-inch 4K UHD monitor with HDR support and vibrant color reproduction for professional work and entertainment."},
        {"name": "Smartwatch", "description": "Stylish smartwatch with fitness tracking, heart rate monitoring, and customizable watch faces."},
        {"name": "USB-C Hub", "description": "Multi-port USB-C hub with HDMI output, USB 3.0 ports, and SD card reader for enhanced connectivity."},
        {"name": "Mechanical Keyboard", "description": "Durable mechanical keyboard with tactile switches and customizable backlighting for precision typing."},
        {"name": "Bluetooth Speaker", "description": "Compact Bluetooth speaker with deep bass and long-lasting battery. Ideal for outdoor activities."},
        {"name": "Webcam", "description": "1080p HD webcam with built-in microphone and wide-angle lens for high-quality video calls."},
        {"name": "Graphics Tablet", "description": "Pressure-sensitive graphics tablet for digital artists, with customizable shortcut keys."},
        {"name": "External Hard Drive", "description": "Reliable 2TB external hard drive with fast data transfer speeds and compact design."},
        {"name": "Wi-Fi Router", "description": "High-speed Wi-Fi router with dual-band support and wide coverage for seamless internet connectivity."},
        {"name": "Laptop Stand", "description": "Adjustable laptop stand with cooling design and ergonomic angles for comfortable use."},
        {"name": "VR Headset", "description": "Virtual reality headset with stunning visuals and immersive gaming experience."},
        {"name": "Docking Station", "description": "All-in-one docking station with multiple USB ports, Ethernet, and dual monitor support."},
        {"name": "Smart Home Hub", "description": "Smart home hub for controlling connected devices with voice commands or a mobile app."},
        {"name": "Portable Projector", "description": "Compact projector with HD resolution and wireless screen mirroring for presentations and movies."},
        {"name": "3D Printer", "description": "High-precision 3D printer with user-friendly interface and versatile filament compatibility."},
        {"name": "USB Flash Drive", "description": "32GB USB flash drive with fast read and write speeds. Small and easy to carry."},
        {"name": "Noise-Canceling Microphone", "description": "Studio-quality microphone with noise-canceling technology for clear audio recordings."},
        {"name": "Smart Thermostat", "description": "Programmable smart thermostat with energy-saving features and remote control via app."},
        {"name": "Wireless Charging Pad", "description": "Fast wireless charging pad compatible with all Qi-enabled devices."},
        {"name": "Gaming Headset", "description": "Over-ear gaming headset with surround sound and noise-isolating microphone."},
        {"name": "E-Reader", "description": "Lightweight e-reader with a glare-free screen and adjustable brightness for comfortable reading."},
        {"name": "Mini PC", "description": "Compact and powerful mini PC with multiple connectivity options for home and office use."},
        {"name": "Dash Cam", "description": "Full HD dash cam with wide-angle lens and night vision for secure driving."},
        {"name": "Ergonomic Mouse", "description": "Ergonomically designed mouse for reducing wrist strain and enhancing productivity."},
        {"name": "Standing Desk Converter", "description": "Adjustable standing desk converter for a healthier and more comfortable workspace."},
        {"name": "Surge Protector", "description": "Advanced surge protector with multiple outlets and USB charging ports."},
        {"name": "Smart Doorbell", "description": "Smart video doorbell with motion detection and two-way audio for enhanced security."},
        {"name": "Power Bank", "description": "Portable power bank with 20000mAh capacity for charging devices on the go."},
        {"name": "Noise-Canceling Earbuds", "description": "Compact earbuds with active noise canceling and superior sound quality."},
        {"name": "Smart Light Bulbs", "description": "Energy-efficient smart bulbs with adjustable brightness and color temperature."},
        {"name": "Portable Monitor", "description": "Slim and lightweight portable monitor with USB-C connectivity for dual-screen setups."},
        {"name": "Action Camera", "description": "Waterproof action camera with 4K video recording and image stabilization."},
        {"name": "Smart Scale", "description": "Digital smart scale with body composition analysis and app integration."},
        {"name": "Cable Organizer", "description": "Compact and portable cable organizer for keeping your workspace tidy."},
        {"name": "Network Switch", "description": "High-performance network switch with multiple ports for stable wired connections."},
        {"name": "Fingerprint Scanner", "description": "USB fingerprint scanner for secure and quick authentication."},
        {"name": "Desktop Microphone", "description": "Desktop microphone with noise reduction for streaming and video conferencing."},
        {"name": "Gaming Chair", "description": "Ergonomic gaming chair with adjustable lumbar support and recline functionality."},
        {"name": "Drone", "description": "Compact drone with HD camera and easy-to-use controls for aerial photography."},
        {"name": "Portable Printer", "description": "Portable photo printer with wireless connectivity and compact design."},
        {"name": "Tablet Stand", "description": "Adjustable tablet stand with sturdy build and multiple viewing angles."},
        {"name": "LED Desk Lamp", "description": "Energy-efficient LED desk lamp with adjustable brightness and flexible arm."},
        {"name": "External DVD Drive", "description": "Slim external DVD drive with plug-and-play functionality for laptops."},
        {"name": "Smart Air Purifier", "description": "Smart air purifier with HEPA filter and real-time air quality monitoring."},
        {"name": "HDMI Cable", "description": "High-speed HDMI cable with gold-plated connectors for reliable video transmission."},
    ]

    # Create products
    if Product.objects.count() == 0:
        print("Seeding 50 products...")
        for product in product_data:
            Product.objects.create(
                name=product["name"],
                description=product["description"],
                price=Decimal(randint(100, 1000))
            )
        print("Products seeded successfully.")
    else:
        print("Products already exist, skipping seeding.")

    # List of customer data
    customer_data = [
        {"name": "Tech Corp", "vat_id": "12345678901", "street": "Main St 1", "city": "Zagreb", "country": "Croatia"},
        {"name": "Innovation Ltd", "vat_id": "98765432109", "street": "Innovation Way 5", "city": "Split", "country": "Croatia"},
        {"name": "Global Solutions", "vat_id": "55566677788", "street": "Market Square 10", "city": "Rijeka", "country": "Croatia"},
        {"name": "Eco Friendly S.A.", "vat_id": "11122233344", "street": "Green Road 2", "city": "Osijek", "country": "Croatia"},
        {"name": "Cyber Security Inc", "vat_id": "99988877766", "street": "Safe Avenue 12", "city": "Zadar", "country": "Croatia"},
    ]

    # Create customers
    if Customer.objects.count() == 0:
        print("Seeding 5 customers...")
        for customer in customer_data:
            Customer.objects.create(**customer)
        print("Customers seeded successfully.")
    else:
        print("Customers already exist, skipping seeding.")

    # Get superuser account
    superuser = User.objects.filter(is_superuser=True).first()
    if not superuser:
        print("Superuser account not found. Please create one first.")
        return

    # Create offers
    if Offer.objects.count() == 0:
        print("Seeding 15 offers...")
        products = list(Product.objects.all())
        customers = list(Customer.objects.all())
        for i in range(1, 16):
            offer_date = datetime.now() - timedelta(days=randint(1, 30))
            selected_products = [choice(products) for _ in range(randint(3, 7))]

            sub_total = sum(p.price for p in selected_products)
            tax = sub_total * Decimal("0.2")  # 20% tax
            total = sub_total + tax

            offer = Offer.objects.create(
                created_by=superuser,
                customer=choice(customers),
                date=offer_date.date(),
                sub_total=sub_total,
                tax=tax,
                total=total
            )

            for product in selected_products:
                OfferItem.objects.create(
                    offer=offer,
                    product=product,
                    quantity=randint(1, 3)
                )
        print("Offers seeded successfully.")
    else:
        print("Offers already exist, skipping seeding.")
