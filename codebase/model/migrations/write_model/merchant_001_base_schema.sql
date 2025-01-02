

-- Client

CREATE TABLE merchant_client (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    platform_id UUID NOT NULL UNIQUE
);

-- Payment Processor

CREATE TABLE merchant_payment_processor (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    name VARCHAR(254) NOT NULL UNIQUE,
    vostro_id UUID NOT NULL UNIQUE
);


-- SKU

CREATE TABLE merchant_sku (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    name VARCHAR(254) NOT NULL UNIQUE,
    price INTEGER NOT NULL
);

-- Transaction

CREATE TABLE merchant_transaction (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    client_id INTEGER NULL,
    CONSTRAINT merchant_transaction_fk_client_id
        FOREIGN KEY(client_id) 
	    REFERENCES merchant_client(id), 

    timestamp TIMESTAMPTZ NOT NULL,

    total_before_tax INTEGER NOT NULL,
    sales_tax INTEGER NOT NULL,
    total_after_tax INTEGER NOT NULL,

    currency VARCHAR(3) NOT NULL
);


-- TransactionPayment

CREATE TABLE merchant_transaction_payment (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    transaction_id INTEGER NOT NULL,
    CONSTRAINT merchant_transaction_line_fk_transaction_id
        FOREIGN KEY(transaction_id) 
	    REFERENCES merchant_transaction(id), 

    timestamp TIMESTAMPTZ NOT NULL,

    payment_amount INTEGER NOT NULL,
    payment_currency VARCHAR(3) NOT NULL,

    payment_processor_id INTEGER NOT NULL,
    CONSTRAINT merchant_transaction_payment_fk_payment_processor_id
        FOREIGN KEY(payment_processor_id) 
	    REFERENCES merchant_payment_processor(id), 

    payment_processor_reference VARCHAR(254) NOT NULL
);

-- TransactionLine

CREATE TABLE merchant_transaction_line (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    transaction_id INTEGER NOT NULL,
    CONSTRAINT merchant_transaction_line_fk_transaction_id
        FOREIGN KEY(transaction_id) 
	    REFERENCES merchant_transaction(id), 

    sku_id INTEGER NOT NULL,
    CONSTRAINT merchant_transaction_line_fk_sku_id
        FOREIGN KEY(sku_id) 
	    REFERENCES merchant_sku(id), 

    unit_count INTEGER NOT NULL,
    total INTEGER NOT NULL
);

-- TransactionReceipt

CREATE TABLE merchant_transaction_receipt (

    id INTEGER GENERATED ALWAYS AS IDENTITY,
        PRIMARY KEY(id),

    transaction_id INTEGER NOT NULL,
    CONSTRAINT merchant_transaction_receipt_fk_transaction_id
        FOREIGN KEY(transaction_id) 
	    REFERENCES merchant_transaction(id)
);

