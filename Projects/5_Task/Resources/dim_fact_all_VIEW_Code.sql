-- @AUTHOR	 	Lennard Becker
-- @DATE		2023-06-02
-- @Version		VBA_prep version
-- Changelog
--				2023-06-01	Code initialized
--				2023-06-02	comments added

-- ============================================ --
-- @VIEW		all_fact_dim
-- @CONTENT		contains all fact- and dimension-tables existing in database
-- @ADDITIONS	preparation for VBA-related task; View was used to export all data in 'export_DB.csv' file
--				following instruction was used to perform the export: https://www.easeus.com/sql-database-recovery/export-ms-sql-server-to-csv.html#:~:text=Open%20SQL%20Server%20Management%20Studio,export%20table%20data%20in%20CSV.

CREATE VIEW all_fact_dim
AS
-- all select columns have their related table as prefix, just for better understanding, technically not necessary
SELECT
	  fact_survey.surveyID_pk,
	  dim_pollster.organization,
	  fact_survey.startDate,
	  startQ.categorie AS startQuartal,
	  fact_survey.endDate,
	  endQ.categorie AS endQuartal,
	  fact_survey.sampleSize,
	  dim_categorieSampleSize.categorie AS sampleSizeCategorie,
	  dim_characteristicVoters.votersType,
	  dim_basicResultset.approve,
	  approvalBasic.categorie AS approveCategorie,
	  dim_basicResultset.disapprove,
	  disapprovalBasic.categorie AS disapproveCategorie,
	  dim_basicResultset.unsure,
	  dim_extendedResultset.approveDemocrats,
	  approvalDemocrats.categorie AS democratsApproveCategorie,
	  dim_extendedResultset.approveRepublicans,
	  approvalRepublican.categorie AS republicanApproveCategorie,
	  dim_questionnaire.text,
	  fact_survey.url
-- initial fact table
FROM mueller.dbo.fact_survey
-- basic information
LEFT JOIN mueller.dbo.dim_pollster
	ON pollsterID_fk = pollsterID_pk
Left JOIN mueller.dbo.dim_questionnaire
	ON textID_fk = textID_pk
LEFT JOIN mueller.dbo.dim_characteristicVoters
	ON population_fk = characteristicVotersID_pk
LEFT JOIN mueller.dbo.dim_categorieSampleSize
	ON sampleSizeCategorie_fk = categorieSampleSizeID_pk
-- basic results and related categories -> alias where used so that each (approve, disapprove) can have their related categorie
-- every alias used is marked with '-- alias' behind it
LEFT JOIN mueller.dbo.dim_basicResultset
	ON mueller.dbo.dim_basicResultset.surveyID_fk = surveyID_pk
LEFT JOIN mueller.dbo.dim_categorieVotes approvalBasic	-- alias 
	ON approveCategorie_fk = approvalBasic.categorieVotesID_pk
LEFT JOIN mueller.dbo.dim_categorieVotes disapprovalBasic -- alias
	ON disapproveCategorie_fk = disapprovalBasic.categorieVotesID_pk
-- extended results and related categories
LEFT JOIN mueller.dbo.dim_extendedResultset
	ON mueller.dbo.dim_extendedResultset.surveyID_fk = surveyID_pk
LEFT JOIN mueller.dbo.dim_categorieVotes approvalDemocrats -- alias
	ON approveDemocratsCategorie_fk = approvalDemocrats.categorieVotesID_pk
LEFT JOIN mueller.dbo.dim_categorieVotes approvalRepublican -- alias
	ON approveRepublicansCategorie_fk = approvalRepublican.categorieVotesID_pk
-- startQ and endQ are aliases so both the start-date and end-date get their sperate quarter
LEFT JOIN mueller.dbo.dim_categorieDate startQ -- alias
	ON startDateQuartal_fk = startQ.categorieDateID_pk
LEFT JOIN mueller.dbo.dim_categorieDate endQ -- alias
	ON endDateQuartal_fk = endQ.categorieDateID_pk
;