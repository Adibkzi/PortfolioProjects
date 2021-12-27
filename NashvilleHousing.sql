/*
Cleaning Data in SQL Queries
*/

Select *
From PortfolioProject.dbo.NashvilleHousing
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Standardize Date Format
Select SaleDateConverted , CONVERT(Date,SaleDate)
From PortfolioProject.dbo.NashvilleHousing

Update NashvilleHousing
SET SaleDate = CONVERT(Date,SaleDate)

ALTER TABLE NashvilleHousing
Add SaleDateConverted Date;

Update NashvilleHousing
SET SaleDateConverted = CONVERT(Date,SaleDate)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Populate Property Address data
Select * 
From PortfolioProject.dbo.NashvilleHousing
--Where PropertyAddress is null 
order by ParcelID

Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress,b.PropertyAddress)
From PortfolioProject.dbo.NashvilleHousing a
JOIN PortfolioProject.dbo.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null

Update a
SET PropertyAddress = ISNULL(a.PropertyAddress,b.PropertyAddress)
From PortfolioProject.dbo.NashvilleHousing a
JOIN PortfolioProject.dbo.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null
----------------------------------------------------------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)
Select  PropertyAddress 
From PortfolioProject.dbo.NashvilleHousing
--Where PropertyAddress is null 
--order by ParcelID

Select 
Substring(PropertyAddress, 1, CHARINDEX(',' , PropertyAddress) -1) as Address
, Substring(PropertyAddress,  CHARINDEX(',' , PropertyAddress) + 1, LEN(PropertyAddress)) as Address

From PortfolioProject.dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
Add PropertySplitAddress Nvarchar(255);

Update NashvilleHousing
SET PropertySplitAddress = Substring(PropertyAddress, 1, CHARINDEX(',' , PropertyAddress) -1)


ALTER TABLE NashvilleHousing
Add PropertySplitCity Nvarchar(255);

Update NashvilleHousing
SET PropertySplitCity =  Substring(PropertyAddress,  CHARINDEX(',' , PropertyAddress) + 1, LEN(PropertyAddress))

select * 
From PortfolioProject.dbo.NashvilleHousing 

select OwnerAddress
from  PortfolioProject.dbo.NashvilleHousing 

select 
parsename(REPLACE(OwnerAddress,',', '.'), 3)
,parsename(REPLACE(OwnerAddress,',', '.'), 2)
,parsename(REPLACE(OwnerAddress,',', '.'), 1)
From PortfolioProject.dbo.NashvilleHousing 



ALTER TABLE NashvilleHousing
Add OwnerSplitAddress Nvarchar(255);

Update NashvilleHousing
SET OwnerSplitAddress = parsename(REPLACE(OwnerAddress,',', '.'), 3)


ALTER TABLE NashvilleHousing
Add OwnerSplitCity Nvarchar(255);

Update NashvilleHousing
SET OwnerSplitCity = parsename(REPLACE(OwnerAddress,',', '.'), 2)

alter table NashvilleHousing
Add OwnerSplitState nvarchar(255);

update NashvilleHousing 
set OwnerSplitState =  parsename(REPLACE(OwnerAddress,',', '.'), 1)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Delete Unused Columns

Select *
From PortfolioProject.dbo.NashvilleHousing


ALTER TABLE PortfolioProject.dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate, SoldAsVacant
