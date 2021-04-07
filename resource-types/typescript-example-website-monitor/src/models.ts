// This is a generated file. Modifications will be overwritten.
import { BaseModel, Dict, integer, Integer, Optional, transformValue } from 'cfn-rpdk';
import { Exclude, Expose, Type, Transform } from 'class-transformer';

export class ResourceModel extends BaseModel {
    ['constructor']: typeof ResourceModel;

    @Exclude()
    public static readonly TYPE_NAME: string = 'Example::Monitoring::Website';

    @Exclude()
    protected readonly IDENTIFIER_KEY_ID: string = '/properties/Id';
    @Exclude()
    protected readonly IDENTIFIER_KEY_NAME: string = '/properties/Name';

    @Expose({ name: 'Id' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'id', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    id?: Optional<string>;
    @Expose({ name: 'ApiKey' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'apiKey', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    apiKey?: Optional<string>;
    @Expose({ name: 'EndpointRegion' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'endpointRegion', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    endpointRegion?: Optional<string>;
    @Expose({ name: 'Kind' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'kind', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    kind?: Optional<string>;
    @Expose({ name: 'Name' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'name', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    name?: Optional<string>;
    @Expose({ name: 'Uri' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'uri', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    uri?: Optional<string>;
    @Expose({ name: 'Frequency' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(Integer, 'frequency', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    frequency?: Optional<integer>;
    @Expose({ name: 'Locations' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'locations', value, obj, [Array]),
        {
            toClassOnly: true,
        }
    )
    locations?: Optional<Array<string>>;
    @Expose({ name: 'Status' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'status', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    status?: Optional<string>;
    @Expose({ name: 'SlaThreshold' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(Number, 'slaThreshold', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    slaThreshold?: Optional<number>;

    @Exclude()
    public getPrimaryIdentifier(): Dict {
        const identifier: Dict = {};
        if (this.id != null) {
            identifier[this.IDENTIFIER_KEY_ID] = this.id;
        }

        // only return the identifier if it can be used, i.e. if all components are present
        return Object.keys(identifier).length === 1 ? identifier : null;
    }

    @Exclude()
    public getAdditionalIdentifiers(): Array<Dict> {
        const identifiers: Array<Dict> = new Array<Dict>();
        if (this.getIdentifier_Name() != null) {
            identifiers.push(this.getIdentifier_Name());
        }
        // only return the identifiers if any can be used
        return identifiers.length === 0 ? null : identifiers;
    }

    @Exclude()
    public getIdentifier_Name(): Dict {
        const identifier: Dict = {};
        if ((this as any).name != null) {
            identifier[this.IDENTIFIER_KEY_NAME] = (this as any).name;
        }

        // only return the identifier if it can be used, i.e. if all components are present
        return Object.keys(identifier).length === 1 ? identifier : null;
    }
}

